


def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

@smart_div
def div(a,b):
    return a/b

# print(div(2,4))


#Asyn


import asyncio
import time


async def fetch_data(name: str, delay: float) -> str:
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} completed")
    return f"{name} result"


async def sequential():
    result_a = await fetch_data("Task A", 2)
    result_b = await fetch_data("Task B", 1)
    return [result_a, result_b]


async def concurrent():
    return await asyncio.gather(
        fetch_data("Task A", 2),
        fetch_data("Task B", 1),
    )


async def main():
    start = time.perf_counter()
    results = await sequential()
    print("Sequential:", results)
    print(f"Time: {time.perf_counter() - start:.2f}s")

    start = time.perf_counter()
    results = await concurrent()
    print("Concurrent:", results)
    print(f"Time: {time.perf_counter() - start:.2f}s")


# asyncio.run(main())

