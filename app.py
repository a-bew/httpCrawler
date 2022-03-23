# Simple example to crawl http urls in parallel
import aiohttp
import asyncio
import time


async def get_req(page_no):
    print("called at time1: " + str(time.time()))
    async with aiohttp.ClientSession() as session:
        async with session.get("http://reqres.in/api/users?page=" + str(page_no), headers={}) as resp:
            print("called at time2: " + str(time.time()))
            return await resp.json()


async def fetch_all_urls():
    results = await asyncio.gather(*[get_req(page_no) for page_no in range(1, 5)], return_exceptions=True)
    # results = [await get_req(page_no) for page_no in range(1, 5)]
    for result in results:
        print('page: %s, size: %s' % (result['page'], len(result['data'])))
    return results


def get_htmls():
    loop = asyncio.get_event_loop()
    htmls = loop.run_until_complete(fetch_all_urls())
    return htmls


start = time.time()
print("start time: " + str(start))
get_htmls()
print("time taken: " + str(time.time() - start))