import aiohttp
import asyncio

class KavenegarAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.kavenegar.com/v1/{}/sms/send.json'.format(api_key)
    
    async def sms_send(self, params):
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url, data=params) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(f"Failed with status code {response.status}")

async def Send(receptor, message):
    try:
        api = KavenegarAPI('6E34613565616E70583476624452665A4630646A38772B3465467747464D38686B536B4B754F35465371493D')
        params = {
            'sender': '90003072',
            'receptor': receptor,
            'message': message
        }
        response = await api.sms_send(params)
        print(response)
    except Exception as e:
        print(f"Error: {e}")