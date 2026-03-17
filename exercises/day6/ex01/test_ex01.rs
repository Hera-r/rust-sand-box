    #[test]
    fn test_binary_search() {
        assert_eq!(binary_search(&[1, 3, 5, 7, 9], 7), Some(3));
        assert_eq!(binary_search(&[1, 3, 5, 7, 9], 4), None);
        let big_vec: Vec<i32> = (0..10_000).collect();
        assert_eq!(binary_search(&big_vec, 5000), Some(5000));
        assert_eq!(binary_search(&big_vec, -1), None);
    }
