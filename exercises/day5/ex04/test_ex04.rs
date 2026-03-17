    #[test]
    fn test_fast_power() {
        assert_eq!(fast_power(2, 10, 1000), 24);
        assert_eq!(fast_power(3, 5, 10), 3);
        assert_eq!(fast_power(5, 0, 7), 1);
        assert_eq!(fast_power(7, 2, 50), 49);
        assert_eq!(fast_power(123, 456, 1), 0);
    }
