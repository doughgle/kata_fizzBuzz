/*
 * fizzbuzz.c
 *
 *  Created on: Jul 29, 2013
 *      Author: HP
 */
#include <stdio.h>

int isDivisableBy3(int number) {
	return (number % 3) == 0;
}

int isDivisableBy5(int number) {
	return (number % 5) == 0;
}

const char* FizzBuzz_toString(int number)
{
	static char numberAsString[] = "9223372036854775807";
	if(isDivisableBy3(number) && isDivisableBy5(number))
	{
		sprintf(numberAsString, "FizzBuzz");
	}
	else if (isDivisableBy3(number))
	{
		sprintf(numberAsString, "Fizz");
	}
	else if (isDivisableBy5(number))
	{
		sprintf(numberAsString, "Buzz");
	}
	else
	{
		sprintf(numberAsString, "%d", number);
	}
	return (const char*)numberAsString;
}
