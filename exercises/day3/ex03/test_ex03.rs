    #[test]
    fn test_list_new() {
        let list: List = List::new();
        assert_eq!(list.len(), 0);
    }

    #[test]
    fn test_list_push() {
        let list = List::new().push(1).push(2).push(3);
        assert_eq!(list.len(), 3);
    }

    #[test]
    fn test_list_head() {
        let list = List::new().push(10).push(20);
        assert_eq!(list.head(), Some(20));
    }

    #[test]
    fn test_list_head_empty() {
        let list = List::new();
        assert_eq!(list.head(), None);
    }

    #[test]
    fn test_list_to_vec() {
        let list = List::new().push(1).push(2).push(3);
        assert_eq!(list.to_vec(), vec![3, 2, 1]);
    }

    #[test]
    fn test_list_dynamic() {
        let mut list = List::new();
        for i in 0..10 {
            list = list.push(i);
        }
        assert_eq!(list.len(), 10);
        assert_eq!(list.head(), Some(9));
    }
