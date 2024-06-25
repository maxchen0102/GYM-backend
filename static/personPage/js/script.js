// myapp/static/myapp/js/scripts.js

$(document).ready(function() {
    $('#test_li_1').each(function(index, element) {
        // `index` 是當前元素的索引
        // `element` 是當前 DOM 元素
        var id = $(this).data('id');  // `this` 是當前 DOM 元素，轉換為 jQuery 對象後，可以使用 jQuery 方法
        var category = $(this).data('category');
        console.log('Index:', index, 'ID:', id, 'Category:', category);
    });

    // 示例操作：點擊列表項時顯示其 ID 和類別
    $('#test_li_1').on('click', function() {
        var id = $(this).data('id');
        var category = $(this).data('category');
        alert('ID: ' + id + '\nCategory: ' + category);
    });
});


