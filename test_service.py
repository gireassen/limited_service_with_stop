import requests
import time
import sys

SERVER_URL = "http://localhost:8008"
MAX_REQUESTS = 10

def test_webhook_service():
    print(f"Testing webhook service at {SERVER_URL}")
    print(f"Expecting service to stop after {MAX_REQUESTS} requests")
    
    successful_requests = 0
    
    for i in range(1, MAX_REQUESTS + 2):  # +2 чтобы проверить 11-й запрос
        try:
            response = requests.post(SERVER_URL, timeout=5)
            if response.status_code == 200:
                successful_requests += 1
                print(f"Request {i}: SUCCESS - {response.text}")
            elif response.status_code == 503:
                print(f"Request {i}: SERVICE STOPPED (as expected) - {response.text}")
                break
        except requests.exceptions.RequestException as e:
            print(f"Request {i}: FAILED - Service unavailable ({str(e)})")
            break
        
        time.sleep(0.1)  # небольшая задержка между запросами
    
    print("\nTest results:")
    print(f"Successful requests: {successful_requests}/{MAX_REQUESTS}")
    
    if successful_requests == MAX_REQUESTS:
        print("✅ Test passed - service stopped after 10 requests")
        return True
    else:
        print("❌ Test failed - unexpected behavior")
        return False

if __name__ == "__main__":
    if not test_webhook_service():
        sys.exit(1)