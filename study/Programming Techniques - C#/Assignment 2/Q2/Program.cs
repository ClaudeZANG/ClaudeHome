using System;
using System.Collections.Generic;
using System.Linq;

namespace ItemPriceManagement
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Item> itemList = new List<Item>
            {
                new Item("Milk", 1, "S456"),
                new Item("Bread", 2, "B34")
            };

            List<Price> priceList = new List<Price>
            {
                new Price(1, 7.99M),
                new Price(2, 3.15M)
            };

            var itemPrices = from item in itemList
                             join price in priceList on item.Id equals price.Id
                             select new { item.Iname, price.ItemPrice };

            Console.WriteLine("Item Prices:");
            foreach (var itemPrice in itemPrices)
            {
                Console.WriteLine($"{itemPrice.Iname} - {itemPrice.ItemPrice:C}");
            }

            Console.WriteLine("Enter item name:");
            string itemName = Console.ReadLine();
            var itemPriceResult = itemPrices.FirstOrDefault(ip => ip.Iname.Equals(itemName, StringComparison.OrdinalIgnoreCase));

            if (itemPriceResult != null)
            {
                Console.WriteLine($"The price of {itemPriceResult.Iname} is {itemPriceResult.ItemPrice:C}");
            }
            else
            {
                Console.WriteLine("Item not found.");
            }
        }
    }
}
