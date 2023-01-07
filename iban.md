An IBAN-compliant account number consists of:

a two-letter country code taken from the ISO 3166-1 standard (e.g., FR for France, GB for the United Kingdom, DE for Germany, and so on)

two check digits used to perform the validity checks – fast and simple, but not fully reliable, tests, showing whether a number is invalid (distorted by a typo) or seems to be good;

the actual account number (up to 30 alphanumeric characters – the length of that part depends on the country)

The standard says that validation requires the following steps (according to Wikipedia):

(step 1) Check that the total IBAN length is correct as per the country (this program won't do that, but you can modify the code to meet this requirement if you wish; note: you have to teach the code all the lengths used in Europe)

(step 2) Move the four initial characters to the end of the string (i.e., the country code and the check digits)

(step 3) Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11 ... Z = 35;

(step 4) Interpret the string as a decimal integer and compute the remainder of that number on division by 97; If the remainder is 1, the check digit test is passed and the IBAN might be valid.