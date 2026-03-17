    #[test]
    fn test_factorial_0() {
        assert_eq!(factorial(0), 1);
    }

    #[test]
    fn test_factorial_1() {
        assert_eq!(factorial(1), 1);
    }

    #[test]
    fn test_factorial_5() {
        assert_eq!(factorial(5), 120);
    }

    #[test]
    fn test_factorial_10() {
        assert_eq!(factorial(10), 3628800);
    }

    #[test]
    fn test_factorial_dynamic() {
        let expected: Vec<u64> = vec![1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600];
        for (i, &exp) in expected.iter().enumerate() {
            assert_eq!(factorial(i as u64), exp, "Failed for factorial({})", i);
        }
    }
