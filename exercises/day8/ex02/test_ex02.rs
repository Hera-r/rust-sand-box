    #[test]
    fn test_merge_sorted() {
        assert_eq!(merge_sorted(&[1,3,5], &[2,4,6]), vec![1,2,3,4,5,6]);
        assert_eq!(merge_sorted(&[1,2,3], &[]), vec![1,2,3]);
        assert_eq!(merge_sorted(&[], &[4,5]), vec![4,5]);
    }
