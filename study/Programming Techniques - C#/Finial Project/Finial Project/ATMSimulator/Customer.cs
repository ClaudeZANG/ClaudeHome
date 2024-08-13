namespace ATMSimulator
{
    public class Customer
    {
        public string Name { get; set; }
        public string PIN { get; set; }

        public Customer(string name, string pin)
        {
            Name = name;
            PIN = pin;
        }
    }
}
