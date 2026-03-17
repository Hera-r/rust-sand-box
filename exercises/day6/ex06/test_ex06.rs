    #[test]
    fn test_graph_bfs() {
        let graph = vec![
            vec![1, 2], // 0
            vec![0, 3], // 1
            vec![0],    // 2
            vec![1]     // 3
        ];
        assert_eq!(bfs(&graph, 0), vec![0, 1, 2, 3]);
        
        let disconnected = vec![
            vec![1],
            vec![0],
            vec![3],
            vec![2]
        ];
        assert_eq!(bfs(&disconnected, 0), vec![0, 1]);
    }
