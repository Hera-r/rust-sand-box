    #[test]
    fn test_max_subarray() {
        assert_eq!(max_subarray(&[-2,1,-3,4,-1,2,1,-5,4]), 6);
        assert_eq!(max_subarray(&[1]), 1);
        assert_eq!(max_subarray(&[-1,-2,-3]), -1);
        assert_eq!(max_subarray(&[5,4,-1,7,8]), 23);
    }
