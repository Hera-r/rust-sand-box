    #[test]
    fn test_is_prime() {
        assert_eq!(is_prime(2), true);
        assert_eq!(is_prime(3), true);
        assert_eq!(is_prime(4), false);
        assert_eq!(is_prime(17), true);
        assert_eq!(is_prime(1), false);
        assert_eq!(is_prime(0), false);
        assert_eq!(is_prime(97), true);
        assert_eq!(is_prime(100), false);
    }
