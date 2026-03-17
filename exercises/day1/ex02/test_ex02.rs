    #[test]
    fn test_is_even_true() {
        assert_eq!(is_even(4), true);
    }

    #[test]
    fn test_is_even_false() {
        assert_eq!(is_even(7), false);
    }

    #[test]
    fn test_is_even_zero() {
        assert_eq!(is_even(0), true);
    }

    #[test]
    fn test_is_even_negative() {
        assert_eq!(is_even(-2), true);
        assert_eq!(is_even(-3), false);
    }

    #[test]
    fn test_is_even_dynamic() {
        for i in -50..50 {
            assert_eq!(is_even(i), i % 2 == 0, "Failed for is_even({})", i);
        }
    }
