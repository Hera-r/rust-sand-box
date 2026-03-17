    #[test]
    fn test_gcd() {
        assert_eq!(gcd(48, 18), 6);
        assert_eq!(gcd(101, 103), 1);
        assert_eq!(gcd(54, 24), 6);
        assert_eq!(gcd(7, 0), 7);
        assert_eq!(gcd(0, 5), 5);
        assert_eq!(gcd(0, 0), 0);
    }
