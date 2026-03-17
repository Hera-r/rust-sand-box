    #[test]
    fn test_sort_by_key_basic() {
        let mut data = vec![("banana", 2), ("apple", 1), ("cherry", 3)];
        sort_by_second(&mut data);
        assert_eq!(data, vec![("apple", 1), ("banana", 2), ("cherry", 3)]);
    }

    #[test]
    fn test_sort_by_key_empty() {
        let mut data: Vec<(&str, i32)> = vec![];
        sort_by_second(&mut data);
        assert_eq!(data, Vec::<(&str, i32)>::new());
    }

    #[test]
    fn test_sort_by_key_already_sorted() {
        let mut data = vec![("a", 1), ("b", 2), ("c", 3)];
        sort_by_second(&mut data);
        assert_eq!(data, vec![("a", 1), ("b", 2), ("c", 3)]);
    }

    #[test]
    fn test_sort_by_key_negative() {
        let mut data = vec![("pos", 5), ("neg", -10), ("zero", 0)];
        sort_by_second(&mut data);
        assert_eq!(data, vec![("neg", -10), ("zero", 0), ("pos", 5)]);
    }

    #[test]
    fn test_sort_by_key_dynamic() {
        let mut data: Vec<(&str, i32)> = vec![
            ("e", 50), ("d", 40), ("c", 30), ("b", 20), ("a", 10),
        ];
        sort_by_second(&mut data);
        for i in 1..data.len() {
            assert!(data[i].1 >= data[i-1].1, "Not sorted at index {}", i);
        }
    }
