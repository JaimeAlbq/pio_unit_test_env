#include <unity.h>

void testing_nice_stuffs(void)
{
    TEST_ASSERT_EQUAL(1, 1);
}

/**
 * @brief Add as many testing functions as needed
 * 
 */

void app_main(void)
{
    UNITY_BEGIN();

    RUN_TEST(testing_nice_stuffs);

    /**
     * @brief Call the testing functions here using the RUN_TEST macro
     * 
     */

    UNITY_END();
}