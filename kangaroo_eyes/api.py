import requests
from colorama import Fore, Style, init
from typing import Dict, List, Union
from datetime import datetime
from .utils import get_api_key, loading_animation, print_color
from .const import API_TIMEOUT

class WhoisAPI:
    
    BASE_URL = "https://www.whoisxmlapi.com/whoisserver/WhoisService"
    
    @staticmethod
    def get_historical_ips(domain: str) -> Dict[str, Union[str, Dict, List]]:
        result = {
            "operation": "Historical IP Lookup",
            "domain": domain,
            "status": "pending",
            "api_used": "whoisxmlapi.com"
        }

        try:
            if not domain:
                raise ValueError("Domain cannot be empty")

            loading_animation(f"Fetching historical IPs for {domain}...")
            api_key = get_api_key("WHOISXML")
            
            if not api_key:
                raise Exception("WHOISXML API key not configured")

            params = {
                "apiKey": api_key,
                "domainName": domain,
                "outputFormat": "JSON",
                "type": "historic"
            }

            # Setup session dengan redirect terbatas
            session = requests.Session()
            session.max_redirects = 3
            
            response = session.get(
                WhoisAPI.BASE_URL,
                params=params,
                headers={"Accept": "application/json"},
                timeout=API_TIMEOUT
            )

            if response.status_code == 200:
                parsed_data = WhoisAPI._parse_response(response.json())
                if not parsed_data or "error" in parsed_data:
                    raise ValueError("No historical IP data available for this domain")
            
                result.update({
                    "status": "success",
                    "records": WhoisAPI._parse_response(response.json()),
                    "query_time": datetime.now().isoformat()
                })
            else:
                raise Exception(f"API response: {response.status_code}")
            
        except ValueError as e:
         result.update({
            "status": "failed",
            "error": str(e),
            "suggestion": "Try another domain or check API documentation"
        })

        except requests.exceptions.TooManyRedirects:
            error_msg = "Too many redirects. Please check API endpoint."
            result.update({
                "status": "failed",
                "error": error_msg
            })
            print_color(f"✗ {error_msg}", "error")
        
        except Exception as e:
            result.update({
                "status": "failed",
                "error": str(e)
            })
            print_color(f"✗ API Error: {str(e)}", "error")
        
        return result

    @staticmethod
    def _parse_response(data: Dict) -> Dict[str, List[str]]:
        if not data:
            return {"error": "Empty API response"}
    
    # Format response yang diharapkan dari WHOISXML API
        if 'history' in data and 'ips' in data['history']:
            return {
            year: ips for year, ips in data['history']['ips'].items()
            if ips  # Hanya tahun dengan IP yang valid
        }
    
    # Alternatif parsing untuk format response berbeda
        if 'ips' in data:
            return {
            entry['year']: entry['ips'] 
            for entry in data['ips'] 
            if 'year' in entry and 'ips' in entry
        }
    
        return {"error": "No IP data found in response structure"}

def get_historical_ips(domain: str) -> Dict[str, Union[str, Dict, List]]:
    return WhoisAPI.get_historical_ips(domain)
