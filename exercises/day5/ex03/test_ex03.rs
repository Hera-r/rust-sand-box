    #[test]
    fn test_collatz_length() {
        assert_eq!(collatz_length(1), 0);
        assert_eq!(collatz_length(12), 9);
        assert_eq!(collatz_length(19), 20);
        assert_eq!(collatz_length(27), 111);
    }
