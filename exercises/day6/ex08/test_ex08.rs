    #[test]
    fn test_my_sort() {
        assert_eq!(my_sort(vec![3,1,4,1,5]), vec![1,1,3,4,5]);
        assert_eq!(my_sort(vec![5,4,3,2,1]), vec![1,2,3,4,5]);
        assert_eq!(my_sort(vec![]), Vec::<i32>::new());
        assert_eq!(my_sort(vec![42]), vec![42]);
    }
