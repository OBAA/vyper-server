import json
import logging
import subprocess
import aiofiles
from aiohttp import web
from concurrent.futures import ThreadPoolExecutor

routes = web.RouteTableDef()

@routes.get('/')
async def handle(request):
    try:
        # Check the Vyper compiler version
        result = subprocess.run(
            ['vyper', '--version'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return web.Response(
            text='Vyper Compiler. Version: {} \n'.format(result.stdout))
    except Exception:
        return web.Response(text='Vyper Compiler is down!')

@routes.post('/compile')
async def compile_vyper(request):
    try:
        # Parse the JSON data from the request
        request_data = await request.json()
        
        # Extract the Vyper source code
        vyper_code = ""
        sources = request_data.get('sources', {})
        for key, value in sources.items():
            vyper_code += value.get('content', '')
        if not vyper_code:
            return web.json_response({'status': 'error', 'error': 'No Vyper source code found'}, status=400)
        # Write the Vyper source code to a temporary file
        temp_file_path = '/tmp/contract.vy'
        async with aiofiles.open(temp_file_path, 'w', encoding='utf-8') as f:
            await f.write(vyper_code)
        # Run the Vyper compiler
        result = subprocess.run(
            ['vyper', temp_file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            return web.json_response({'status': 'success', 'output': result.stdout})
        else:
            return web.json_response({'status': 'error', 'error': result.stderr}, status=400)
    except json.JSONDecodeError:
        return web.json_response({'status': 'error', 'error': 'Invalid JSON format'}, status=400)
    except Exception as e:
        return web.json_response({'status': 'error', 'error': str(e)}, status=500)

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    web.run_app(app, host='0.0.0.0', port=8000)
