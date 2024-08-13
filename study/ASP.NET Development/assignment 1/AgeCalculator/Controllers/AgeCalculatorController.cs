using AgeCalculator.Models;
using Microsoft.AspNetCore.Mvc;
using System;

namespace AgeCalculator.Controllers
{
    public class AgeCalculatorController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Calculate(DateTime birthDate)
        {
            var age = CalculateAge(birthDate);
            return View("Index", age);
        }

        private AgeViewModel CalculateAge(DateTime birthDate)
        {
            var now = DateTime.Now;
            var age = new AgeViewModel
            {
                Years = now.Year - birthDate.Year,
                Months = now.Month - birthDate.Month,
                Weeks = (int)((now - birthDate).TotalDays / 7),
                Days = (int)(now - birthDate).TotalDays,
                Hours = (int)(now - birthDate).TotalHours,
                Minutes = (int)(now - birthDate).TotalMinutes,
                Seconds = (int)(now - birthDate).TotalSeconds
            };

            if (now.DayOfYear < birthDate.DayOfYear)
            {
                age.Years--;
                age.Months += 12;
            }

            return age;
        }
    }
}
