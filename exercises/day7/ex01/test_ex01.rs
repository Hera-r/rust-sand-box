    #[test]
    fn test_shared_counter() {
        assert_eq!(shared_counter(4, 100), 400);
        assert_eq!(shared_counter(2, 50), 100);
        assert_eq!(shared_counter(10, 1000), 10000);
    }
