(function () {
  angular
  .module('nourish.storeController', [
  ])
  // Store Controller --- view for individual stores with containing items
  .controller('storeController', function($scope, $state, $location, $stateParams, Stores, Items) {
    $scope.storeName, $scope.storeDescription;
    
    //get store information
    $scope.getStore = function () {
      Stores.getStore($stateParams.storeId).then(function(response){
        $scope.storeName = response.data.name;
        $scope.storeDescription = response.data.description;
      })
    }

    // edit store information
    $scope.updateStore = function(){
      var data = {
        name: $scope.storeName,
        description: $scope.storeDescription
      }
      Stores.updateStore($stateParams.storeId, data).then(function(response){
        $location.path('/');
      })
    }

    // get all items for a particular store
    $scope.getAllItemsFromStore = function () {
      Stores.getStore($stateParams.storeId).then(function(response){
        $scope.storeItems = [];
        $scope.storeName = response.data.name;
        $scope.storeDescription = response.data.description;
        if(response.data.items.length>0){
          for(var i = 0; i<response.data.items.length; i++){
            var id = response.data.items[i].split('items/')[1].split('/')[0]
              Items.getItem(id).then(function(response){
              $scope.storeItems.push(response.data)
            })
          }
        } else {
          // display no items
        }
        
      });
    }


    // add an item for a particular store ---
    $scope.addItem = function () {
      var itemData = {
        name: $scope.itemName,
        comments: $scope.itemComments,
        expiration: $scope.itemExpiration,
        amount: $scope.itemAmount,
        store: $stateParams.storeId
      }

      Items.addItem(itemData).then(function(response){
        $scope.getAllItemsFromStore();
        $scope.itemName = '';
        $scope.itemComments = '';
        $scope.itemExpiration = '';
        $scope.itemAmount = ''; 
      })
    }

    // delete item from store
    $scope.deleteItem = function (itemId) {
      Items.deleteItem(itemId).then(function(response){
        $scope.getAllItemsFromStore();
      })
    }

})

 //Item Controller  
  .controller('itemController', function($scope,$state, $stateParams, $location, Stores, Items){
    // get specific item
    $scope.getItem = function(){
      Items.getItem($stateParams.itemId).then(function(response){
          $scope.itemName = response.data.name;
          $scope.itemComments = response.data.comments;
          $scope.itemExpiration = response.data.expiration;
          $scope.itemStore = response.data.store;
          $scope.itemAmount = response.data.amount;
        })
    }

    //update specfic item
    $scope.updateItem = function(){
      var data = {
        name: $scope.itemName,
        comments: $scope.itemComments,
        expiration: $scope.itemExpiration,
        store: $scope.itemStore,
        amount: $scope.itemAmount
      }
      Items.updateItem($stateParams.itemId, data).then(function(response){
       $location.path('/stores/' + response.data.store);
      })
    }

    //IN PROGRESS
    $scope.getItemsList = function () {
      $scope.items
      Items.getAllItems().then(function(response){
        $scope.items = response.data.results;
      }).then(function(){
        for(var i= 0; i<$scope.items.length; i++){
          Stores.getStore($scope.items[i].store).then(function(response){
            
          })
           
        }
      })   
    }

  })

}).call(this);
