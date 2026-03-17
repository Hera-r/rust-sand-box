    #[test]
    fn test_longest_common_prefix() {
        assert_eq!(longest_common_prefix(&["flower", "flow", "flight"]), "fl");
        assert_eq!(longest_common_prefix(&["dog", "racecar", "car"]), "");
        assert_eq!(longest_common_prefix(&["abc"]), "abc");
    }
