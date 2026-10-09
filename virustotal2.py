import virustotal_python
from pprint import pprint
from base64 import urlsafe_b64encode
import pandas as pd

v_url = "bit.ly/shopeebigsale662"

with virustotal_python.Virustotal("09cb4f8901fdaf4d859dc96a87d596ea1ae419ae1ed2219bb25baf056d5adbb7") as vtotal:
    try:
        resp = vtotal.request("urls", data={"url": v_url}, method="POST")
        # Safe encode URL in base64 format
        # https://developers.virustotal.com/reference/url
        url_id = urlsafe_b64encode(v_url.encode()).decode().strip("=")
        report = vtotal.request(f"urls/{url_id}")
        # pprint(report.object_type)
        # pprint(report.data)
        v_result_url = report.data['attributes']['last_analysis_stats']
        print(v_url)
        print(v_result_url)

    except virustotal_python.VirustotalError as err:
        print(
            f"Failed to send URL: {v_url} for analysis and get the report: {err}")

vt3 = pd.DataFrame(v_result_url, index=[0]).reset_index(drop=True)
count = (((vt3['malicious']+vt3['suspicious']+vt3['undetected']) / (vt3['harmless'] +
         vt3['malicious']+vt3['suspicious']+vt3['undetected']+vt3['timeout'])) * 100)
print('Unsafe percentage: ' + str(round(count[0], 1)) + ' %')
