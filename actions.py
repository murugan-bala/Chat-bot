
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import requests

class ApiAction(Action):
    def name(self):
        return "action_enroll"

    def run(self, dispatcher, tracker, domain):
    #def run(self):
        enroll_type = tracker.get_slot('enroll_type')
        url = "http://lwawstest1.sifylivewire.com/api/enrolcourse"
        headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImIwNmZkYWJiNDlmYTMwMTFhMzZlYmM0YTRhM2Q1ZGZkOWVlZjQ4OWIzNmYxOTIxZjNmOTY2OTlmMDYyYTRhYWFiODExNGQ3N2ZkNmI0NTBmIn0.eyJhdWQiOiIzIiwianRpIjoiYjA2ZmRhYmI0OWZhMzAxMWEzNmViYzRhNGEzZDVkZmQ5ZWVmNDg5YjM2ZjE5MjFmM2Y5NjY5OWYwNjJhNGFhYWI4MTE0ZDc3ZmQ2YjQ1MGYiLCJpYXQiOjE1NjkzODgwNzEsIm5iZiI6MTU2OTM4ODA3MSwiZXhwIjoxNTcwNjg0MDcxLCJzdWIiOiIiLCJzY29wZXMiOltdfQ.I0MUa8B21zx-fo-aeOcuYzGMxG8DFwX3YW-cwRIDXkFCQa615Kxxa_g9ILb5cPWvVg15YplzaZr3z9euwG6Y0SbOdiZUVH9vbK9n4I6NECQmTQdMfkddJ5CyBgHmhrUdnuJHdpSAWSWGQy8RsCS543re42sI9WcA6-WOTIA1iA7gpIiM1vF00Vdlvo0WcKekgLl1cs6cOgAY0a62nJn2iiT5me-LfTcTZHO5t62_BbYldXTssNyZmDqutaQHBArW-M016YDvk6tnaKVvZnIC3HvAMUWPZQgBiOre5upvFXeF6Dklh9CWn17kJELLz6NtMsdmjpvq44UqyRWVOwH4MyPPUQjN3ycf-w6xzjHW7zzkab4d5qX0ITF1_sdcIc5QBZYVu0-RYDvezsIqmlxi_CQfpfgrYEp-tzdzhrbKRAn1PSN5yc3a-_RGTLRe7jiCklqbPQcYhEZkXlUgsw_1B6hs58SM6Ixd1hOraiMkt01AdAkk4iE5dzxKBem6eaWvJeZiZ7e-TJjddL-VBwwjxG1R20RBtPMRVNAlt3NpqCOnzomL86cVmKMKOMI_CO6urlKnp8xRCSYap96NcBJrLOme_HyMP0IFZvGlkDNQNTHaULVi3OeOS-zRkVUQgGpFL6HmjhC_lHIs6AvxVKenLCojkFYVRaT5xZ-uzq-wa4c",
    'saltkey': "ZllZS1Vhd2pIcmlKS1IzcURSS0tOZE0zQzkwQWVyU3IxbXN1MUpHaw==",
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "fd8d64b0-7229-4b61-9b6f-6201ab7047b9,5e6c8a9d-90a1-442d-b104-f99d86ab6e2c",
    'Host': "lwawstest1.sifylivewire.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "112",
    'Cookie': "Tenantname=lwawstest1",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
        payload = "usls=%7B%22user_id%22%3A%22superadmin%40mail.com%22%2C%22course_delivery_id%22%3A%221896%22%2C%20%22course_id%22%3A%222234%22%7D"
        #payload= {"user_id":"superadmin@mail.com","course_delivery_id":"1568", "course_id":"1790"}
        response = requests.request("POST", url, data=payload,headers=headers)
        #print(response.text)
        status=response.json()
        stat=status['data']
        stats=stat['error']
        dispatcher.utter_message("Your status is  {}".format(stats))
        #return [SlotSet("link",link), SlotSet("authors",authors)]
