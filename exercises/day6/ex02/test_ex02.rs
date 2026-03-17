    #[test]
    fn test_max_sliding_window() {
        assert_eq!(max_sliding_window(&[1,3,-1,-3,5,3,6,7], 3), vec![3, 3, 5, 5, 6, 7]);
        assert_eq!(max_sliding_window(&[1], 1), vec![1]);
        assert_eq!(max_sliding_window(&[1,-1], 1), vec![1, -1]);
        assert_eq!(max_sliding_window(&[9,11], 2), vec![11]);
    }
