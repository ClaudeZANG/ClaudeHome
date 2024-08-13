using System.ComponentModel.DataAnnotations;

namespace AddressBook.Models
{
    public class Contact
    {
        public int Id { get; set; }

        [Required]
        public string Name { get; set; }

        [Required]
        [EmailAddress]
        public string Email { get; set; }

        public string PhoneNumber { get; set; }

        public string Address { get; set; }
    }
}
