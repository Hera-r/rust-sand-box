    use std::collections::HashMap;

    #[test]
    fn test_word_count_basic() {
        let result = word_count("hello world hello");
        assert_eq!(result.get("hello"), Some(&2));
        assert_eq!(result.get("world"), Some(&1));
    }

    #[test]
    fn test_word_count_empty() {
        let result = word_count("");
        assert_eq!(result.len(), 0);
    }

    #[test]
    fn test_word_count_single() {
        let result = word_count("rust");
        assert_eq!(result.get("rust"), Some(&1));
        assert_eq!(result.len(), 1);
    }

    #[test]
    fn test_word_count_dynamic() {
        let input = "the cat sat on the mat the cat";
        let result = word_count(input);
        assert_eq!(result.get("the"), Some(&3));
        assert_eq!(result.get("cat"), Some(&2));
        assert_eq!(result.get("sat"), Some(&1));
        assert_eq!(result.get("on"), Some(&1));
        assert_eq!(result.get("mat"), Some(&1));
    }
