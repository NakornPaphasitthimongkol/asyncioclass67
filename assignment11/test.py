import time
import asyncio
from asyncio import Queue


class Customer:
    def __init__(self, customer_id: int, checkout_time: float):
        self.customer_id = customer_id
        self.checkout_time = checkout_time


async def checkout_customer(queue: Queue, cashier_number: int, results: dict):
    while not queue.empty():
        customer: Customer = await queue.get()
        start_time = time.perf_counter()
        print(f"Cashier {cashier_number} is checking out Customer {customer.customer_id}")
        
        # Simulate the checkout time
        await asyncio.sleep(customer.checkout_time)
        
        # Calculate time taken for the customer
        time_taken = round(time.perf_counter() - start_time, 2)
        print(f"Cashier {cashier_number} finished Customer {customer.customer_id} in {time_taken} secs")

        # Store the result for each cashier
        if cashier_number not in results:
            results[cashier_number] = []
        results[cashier_number].append(time_taken)
        
        queue.task_done()


async def customer_generation(queue: Queue, customers: list):
    for customer in customers:
        await queue.put(customer)
        print(f"Customer {customer.customer_id} added to the queue")


async def main():
    # Create a queue that can hold 5 customers at a time
    customer_queue = Queue(5)

    # Define customers and their checkout times as per the table
    customers = [
        Customer(2, 2.4), Customer(3, 4.0), Customer(4, 4.8), 
        Customer(5, 3.6), Customer(10, 4.01)
    ]
    
    # Generate the customers into the queue
    await customer_generation(customer_queue, customers)
    
    # Dictionary to store results for each cashier
    results = {}

    # Define 5 cashiers
    cashiers = [checkout_customer(customer_queue, i, results) for i in range(1, 6)]
    
    # Start processing customers with cashiers
    await asyncio.gather(*cashiers)
    
    # Display results
    for cashier, times in results.items():
        total_time = round(sum(times), 2)
        print(f"Cashier {cashier} took total {total_time} secs for their customers: {times}")

    # Calculate total time for all customers
    total_time_for_all_customers = round(sum([sum(times) for times in results.values()]), 2)
    print(f"\nTotal time for all customers: {total_time_for_all_customers} secs")


if __name__ == "__main__":
    asyncio.run(main())
