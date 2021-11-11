import requests
import time
import asyncio
from aiohttp import ClientSession

urls = ['http://img.netbian.com/file/2021/1008/smallb1da73de2372521b86953f052c0439331633705165.jpg',
        'http://img.netbian.com/file/2021/1006/smalla78c8de3a671c5b31eff23ef4087b2111633531740.jpg',
        'http://img.netbian.com/file/newc/fadf8f4844ebceedaa41956a889608b5.jpg',
        'http://img.netbian.com/file/2021/0813/smallb57661b3edb3464253842fb63bc85ed01628865701.jpg',
        'http://img.netbian.com/file/2021/0725/small39b7280f0ba31a3a7ba3cec9413b4c2e1627224387.jpg',
        'http://img.netbian.com/file/2021/0929/small41dc89d6f11114d53744646def584cf91632925817.jpg',
        'http://img.netbian.com/file/2021/0929/smallba75df9dc0b519053ec5b46b45d5cb541632925732.jpg',
        'http://img.netbian.com/file/2021/0928/smallbfaa05a32284d402dd595df0a68b50901632836519.jpg',
        'http://img.netbian.com/file/2021/0927/small9fba697e773457f162f6f31f4d769fce1632712676.jpg',
        'http://img.netbian.com/file/2021/0925/small7cae9fce77e621ff5629cd018742ecb71632584930.jpg',
        'http://img.netbian.com/file/2021/0923/smallb6a49c2d5812a69194320f528c07b4721632409913.jpg',
        'http://img.netbian.com/file/2021/0923/small059bb426a3a8ef22739e8ad34ab0d88b1632409769.jpg',
        'http://img.netbian.com/file/2021/0916/small0ffcc6afcb65fcc3b2b3c93e6eda1fc11631797931.jpg',
        'http://img.netbian.com/file/2021/0914/smallf2fddbcb7fd5a68a904b0fb466cc22461631630314.jpg',
        'http://img.netbian.com/file/2021/0914/small07c232f81d0b17031a7b294aef030ecd1631628824.jpg',
        'http://img.netbian.com/file/2021/0903/small322039d952a6d914b804264319c8e1cd1630681939.jpg',
        'http://img.netbian.com/file/2021/0902/small7c5eb2eaaad287d7bf190b6fa9d1f4991630597719.jpg',
        'http://img.netbian.com/file/2021/0901/smalldf16a94fafa098c6a2b32aa327e9b57f1630509628.jpg',
        'http://img.netbian.com/file/2021/0826/smallf58d3fa5b888b14c5e98e5f1933f19d21629990503.jpg',
        'http://img.netbian.com/file/2021/0824/smallbafd717bbea60237716abf3e117c698a1629799852.jpg']


# 普通方式下载图片
# def download_image(url):
#     print(url)
#     resp = requests.get(url)
#     with open(f"./img/{int(time.time() * 1000)}.jpg", 'wb') as f:
#         f.write(resp.content)
#         print("download success!")


# 协程方式实现
async def download_image(url):
    print(url)
    async with ClientSession() as session:
        async with session.get(url) as response:
            resp = await response.read()
            with open(f"./img/{int(time.time() * 1000)}.jpg", 'wb') as f:
                f.write(resp)
                print("download success!")


async def main():
    tasks = [download_image(i) for i in urls]
    await asyncio.wait(tasks)  # 等待执行完成所有任务事件


if __name__ == '__main__':
    # for i in urls:
    #     download_image(i)
    asyncio.run(main())
