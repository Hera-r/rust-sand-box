    #[test]
    fn test_add_basic() {
        assert_eq!(add_numbers(2, 3), 5);
    }

    #[test]
    fn test_add_zero() {
        assert_eq!(add_numbers(0, 0), 0);
    }

    #[test]
    fn test_add_negative() {
        assert_eq!(add_numbers(-5, 3), -2);
    }

    #[test]
    fn test_add_large() {
        assert_eq!(add_numbers(1_000_000, 2_000_000), 3_000_000);
    }

    #[test]
    fn test_add_random() {
        // Anti-cheat: dynamic test
        let pairs: Vec<(i32, i32)> = vec![
            (42, 58), (100, -100), (-7, -13), (999, 1),
            (123, 456), (-999, 999), (0, i32::MAX),
        ];
        for (a, b) in pairs {
            assert_eq!(add_numbers(a, b), a + b, "Failed for add_numbers({}, {})", a, b);
        }
    }
