    #[test]
    fn test_lcm() {
        assert_eq!(lcm(21, 6), 42);
        assert_eq!(lcm(4, 6), 12);
        assert_eq!(lcm(15, 20), 60);
        assert_eq!(lcm(7, 5), 35);
        assert_eq!(lcm(0, 5), 0);
    }
