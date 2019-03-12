/**
 * @author: mg12 [http://www.neoease.com/]
 * @update: 2013/01/09
 *
 * IE6/7 need a third-party JSON library to polyfill this feature. [https://github.com/douglascrockford/JSON-js/blob/master/json2.js]
 */

ViewHistory = function() {

	this.config = {
		limit: 10,
		storageKey: 'viewHistory',
		primaryKey: 'url'
	};

	this.cache = {
		localStorage:  null,
		userData:  null,
		attr:  null
	};
};

ViewHistory.prototype = {

	init: function(config) {
		this.config = config || this.config;
		var _self = this;

		// define localStorage
		if (!window.localStorage && (this.cache.userData = document.body) && this.cache.userData.addBehavior && this.cache.userData.addBehavior('#default#userdata')) {
			this.cache.userData.load((this.cache.attr = 'localStorage'));

			this.cache.localStorage = {
				'getItem': function(key) {
					return _self.cache.userData.getAttribute(key);
				},
				'setItem': function(key, value) {
					_self.cache.userData.setAttribute(key, value);
					_self.cache.userData.save(_self.cache.attr);
				}
			};

		} else {
			this.cache.localStorage = window.localStorage;
		}
	},

	addHistory: function(item) {
		var items = this.getHistories();
		for(var i=0, len=items.length; i<len; i++) {
			if(item[this.config.primaryKey] && items[i][this.config.primaryKey] && item[this.config.primaryKey] === items[i][this.config.primaryKey]) {
				items.splice(i, 1);
				break;
			}
		}

		items.push(item);

		if(this.config.limit > 0 && items.length > this.config.limit) {
			items.splice(0, 1);
		}

		var json = JSON.stringify(items);
		this.cache.localStorage.setItem(this.config.storageKey, json);
	},

	getHistories: function() {
		var history = this.cache.localStorage.getItem(this.config.storageKey);
		if(history) {
			return JSON.parse(history);
		}
		return [];
	}
};

if(typeof localStorage !== 'undefined' && typeof JSON !== 'undefined') {
    var viewHistory = new ViewHistory();
    viewHistory.init({
        limit: 5,
        storageKey: 'viewHistory',
        primaryKey: 'url'
    });
}

var wrap = document.getElementById('recently_viewed');
 
// 如果 ViewHistory 的实例存在，并且外层节点存在，则可显示历史浏览记录
if(viewHistory && wrap) {
    // 获取浏览记录
    var histories = viewHistory.getHistories();
 
    // 组装列表
    var list = document.createElement('ol');
    if(histories && histories.length > 0) {
        for(var i=histories.length-1; i>=0; i--) {
            var historyItem = histories[i];
 
            var item = document.createElement('li');
            var itemLink = document.createElement('a');
            itemLink.href = historyItem.url;
            itemLink.innerHTML = historyItem.title;
 
            item.appendChild(itemLink);
            list.appendChild(item);
        }
 
        // 插入页面特定位置
        wrap.appendChild(list);
    }
}