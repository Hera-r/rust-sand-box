    #[test]
    fn test_min_heap() {
        let mut h = MinHeap::new();
        h.push(5);
        h.push(1);
        h.push(3);
        assert_eq!(h.peek(), Some(&1));
        assert_eq!(h.pop(), Some(1));
        assert_eq!(h.pop(), Some(3));
        assert_eq!(h.pop(), Some(5));
        assert_eq!(h.pop(), None);
    }
