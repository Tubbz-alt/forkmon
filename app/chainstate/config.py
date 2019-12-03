nodes_debug = {
    'Geth (Constantinople)': {
    	'url': 'http://localhost:8546',
    	'explorer': "https://etherscan.io/block/%s",
    },
    'Parity (Constantinople)': {
        'url': 'http://localhost:8547',
        'explorer': "https://etherscan.io/block/%s",
    },
}

nodes_prod = {
    'Geth (Upgraded)': {
        'url': 'http://172.31.0.19:8545',
        'explorer': "https://etherscan.io/block/%s",
    },
    'Parity (Upgraded)': {
        'url': 'http://172.31.7.228:8545',
        'explorer': "https://etherscan.io/block/%s",
    },
    'Geth (Non upgraded - erroneous)': {
        'url': 'http://172.31.2.251:8545',
        'explorer': "https://etherscan.io/block/%s",
    },
}
