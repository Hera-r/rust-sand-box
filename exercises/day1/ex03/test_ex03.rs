    #[test]
    fn test_fizzbuzz_3() {
        assert_eq!(fizzbuzz(3), "fizz");
    }

    #[test]
    fn test_fizzbuzz_5() {
        assert_eq!(fizzbuzz(5), "buzz");
    }

    #[test]
    fn test_fizzbuzz_15() {
        assert_eq!(fizzbuzz(15), "fizzbuzz");
    }

    #[test]
    fn test_fizzbuzz_regular() {
        assert_eq!(fizzbuzz(7), "7");
    }

    #[test]
    fn test_fizzbuzz_1() {
        assert_eq!(fizzbuzz(1), "1");
    }

    #[test]
    fn test_fizzbuzz_dynamic() {
        for i in 1..=100 {
            let expected = if i % 15 == 0 {
                "fizzbuzz".to_string()
            } else if i % 3 == 0 {
                "fizz".to_string()
            } else if i % 5 == 0 {
                "buzz".to_string()
            } else {
                i.to_string()
            };
            assert_eq!(fizzbuzz(i), expected, "Failed for fizzbuzz({})", i);
        }
    }
