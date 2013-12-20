/*
 * test_fizzBuzz.c
 *
 *  Created on: Jul 29, 2013
 *      Author: HP
 */
#include "unity.h"
#include "fizzbuzz.h"

void setUp(void)
{

}

void tearDown(void)
{

}

void assertFizz(int number) {
	TEST_ASSERT_EQUAL_STRING("Fizz", FizzBuzz_toString(number));
}

void assertBuzz(const int number) {
	TEST_ASSERT_EQUAL_STRING("Buzz", FizzBuzz_toString(number));
}

void test_given1Returns1AsString(void)
{
	TEST_ASSERT_EQUAL_STRING("1", FizzBuzz_toString(1));
}

void test_given2Returns2AsString(void)
{
	TEST_ASSERT_EQUAL_STRING("2", FizzBuzz_toString(2));
}


void test_given3ReturnsFizz(void)
{
	assertFizz(3);
}

void test_given5ReturnsBuzz(void)
{
	assertBuzz(5);
}

void test_divisableBy3ReturnsFizz(void)
{
	assertFizz(6);
}

void test_divisableBy5ReturnsBuzz(void)
{
	assertBuzz(10);
}

void test_divisableBy3And5ReturnsFizzBuzz(void)
{
	TEST_ASSERT_EQUAL_STRING("FizzBuzz", FizzBuzz_toString(15));
}
