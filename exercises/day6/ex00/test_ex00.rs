    #[test]
    fn test_two_sum() {
        assert_eq!(two_sum(&[1, 2, 7, 11, 15], 9), (1, 2));
        assert_eq!(two_sum(&[2, 3, 4], 6), (0, 2));
        assert_eq!(two_sum(&[1, 5, 8], 13), (1, 2));
    }
