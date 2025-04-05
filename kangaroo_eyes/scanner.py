import socket
import nmap
import whois
from dns import resolver, exception as dns_exception
from typing import Dict, List, Union
from datetime import datetime
from colorama import Style
from .utils import loading_animation, print_color
from .const import API_TIMEOUT

class NetworkScanner:
    def __init__(self):
        self.resolver = resolver.Resolver()
        self.resolver.nameservers = ["8.8.8.8", "1.1.1.1"]  

    def dns_enum(self, domain: str) -> Dict[str, Union[str, List[str]]]:
        result = {
            "operation": "DNS Enumeration",
            "domain": domain,
            "query_time": datetime.now().isoformat(),
            "records": []
        }

        try:
            if not domain:
                raise ValueError("Domain cannot be empty")
            
            loading_animation(f"Resolving DNS for {domain}...")
            
            if not self._is_valid_domain(domain):
                raise ValueError(f"Invalid domain format: {domain}")
            
            answers = self.resolver.resolve(domain, "A")
            ips = [str(rdata.address) for rdata in answers]
            
            result.update({
                "records": ips,
                "count": len(ips),
                "nameservers": self.resolver.nameservers,
                "status": "success"
            })
            
        except dns_exception.DNSException as e:
            result.update({
                "error": f"DNS Resolution Error: {str(e)}",
                "status": "failed"
            })
        except Exception as e:
            result.update({
                "error": f"Unexpected Error: {str(e)}",
                "status": "failed"
            })
        
        return result

    def port_scan(self, target: str, ports: str = '21,22,80,443,3389') -> Dict[str, Union[str, Dict]]:
        result = {
            "operation": "Port Scan",
            "target": target,
            "ports_scanned": ports,
            "query_time": datetime.now().isoformat(),
            "results": {}
        }

        try:
            if not target:
                raise ValueError("Target cannot be empty")
                
            loading_animation(f"Scanning {target}...")
            
            if not (self._is_valid_ip(target) or self._is_valid_domain(target)):
                raise ValueError(f"Invalid target: {target}")
            
            scanner = nmap.PortScanner()
            scanner.scan(target, ports, arguments='-T4')
            
            if not scanner.all_hosts():
                result.update({"status": "No hosts found"})
                return result
                
            for host in scanner.all_hosts():
                host_data = {
                    "hostname": scanner[host].hostname(),
                    "state": scanner[host].state(),
                    "protocols": {}
                }
                
                for proto in scanner[host].all_protocols():
                    host_data["protocols"][proto] = [
                        {
                            "port": port,
                            "state": scanner[host][proto][port]["state"],
                            "service": scanner[host][proto][port].get("name", "unknown")
                        } 
                        for port in scanner[host][proto]
                    ]
                
                result["results"][str(host)] = host_data
                result["status"] = "success"
            
        except nmap.PortScannerError as e:
            result.update({
                "error": f"Nmap Error: {str(e)}",
                "status": "failed"
            })
        except Exception as e:
            result.update({
                "error": f"Unexpected Error: {str(e)}",
                "status": "failed"
            })
        
        return result

    def whois_lookup(self, domain: str) -> Dict[str, Union[str, Dict]]:
        result = {
            "operation": "WHOIS Lookup",
            "domain": domain,
            "query_time": datetime.now().isoformat(),
            "data": {}
        }

        try:
            if not domain:
                raise ValueError("Domain cannot be empty")
                
            loading_animation(f"Checking WHOIS for {domain}...")
            
            if not self._is_valid_domain(domain):
                raise ValueError(f"Invalid domain format: {domain}")
            
            info = whois.whois(domain)
            
            for key, value in info.items():
                if key.startswith('_'):
                    continue
                    
                if isinstance(value, list):
                    value = [str(v) if not isinstance(v, str) else v for v in value]
                elif not isinstance(value, str):
                    value = str(value)
                    
                if value and value not in ['None', '']:
                    result["data"][key] = value
            
            result["status"] = "success"
            
        except whois.parser.PywhoisError as e:
            result.update({
                "error": f"WHOIS Error: {str(e)}",
                "status": "failed"
            })
        except Exception as e:
            result.update({
                "error": f"Unexpected Error: {str(e)}",
                "status": "failed"
            })
        
        return result

    def _is_valid_domain(self, domain: str) -> bool:
        try:
            socket.gethostbyname(domain)
            return True
        except socket.error:
            return False

    def _is_valid_ip(self, ip: str) -> bool:
        try:
            socket.inet_aton(ip)
            return True
        except socket.error:
            return False
