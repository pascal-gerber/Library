#while Threading uses the cores to make a multithread,
#asyncio uses just one core and is lighter than Threading
#the functionalities are very similar if not the same
#time cannot be used in the asyncio module, just in the one threading
#currently running.

import asyncio

#needs to make the functions async
async def first():
    print("one")
    #time.sleep gets exchanged with asyncio.sleep
    await asyncio.sleep(1)
    print("four")

async def second():
    print("two")
    await asyncio.sleep(1)
    print("five")

async def three():
    print("three")
    await asyncio.sleep(1)
    print("six")

#theres a main function that runs multiples asyncs in a row
#can also only have a simple "asyncio.run(function())"
async def main():       # \/ 1       \/ 2      \/ 3
    await asyncio.gather(first(), second(), three())
    #calling a async function requires "await".

#runs the function main()
asyncio.run(main())

