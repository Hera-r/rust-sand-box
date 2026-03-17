    #[test]
    fn test_channel_pipeline() {
        assert_eq!(channel_pipeline(5), vec![2, 4, 6, 8, 10]);
        assert_eq!(channel_pipeline(3), vec![2, 4, 6]);
        assert_eq!(channel_pipeline(0), Vec::<i32>::new());
    }
