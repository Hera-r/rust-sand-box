    use std::collections::HashSet;

    #[test]
    fn test_unique_basic() {
        let mut result = unique_elements(vec![1, 2, 2, 3, 3, 3]);
        result.sort();
        assert_eq!(result, vec![1, 2, 3]);
    }

    #[test]
    fn test_unique_empty() {
        let result: Vec<i32> = unique_elements(vec![]);
        assert_eq!(result, Vec::<i32>::new());
    }

    #[test]
    fn test_unique_all_same() {
        let result = unique_elements(vec![5, 5, 5, 5]);
        assert_eq!(result, vec![5]);
    }

    #[test]
    fn test_unique_already_unique() {
        let mut result = unique_elements(vec![1, 2, 3, 4, 5]);
        result.sort();
        assert_eq!(result, vec![1, 2, 3, 4, 5]);
    }

    #[test]
    fn test_unique_dynamic() {
        let input: Vec<i32> = (0..100).chain(0..100).collect();
        let result = unique_elements(input);
        let set: HashSet<i32> = result.into_iter().collect();
        assert_eq!(set.len(), 100);
    }
