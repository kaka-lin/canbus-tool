WorkerScript.onMessage = function(msg) {
    var data = {'can_id': msg.can_id, 'can_data': msg.can_data};
    msg.model.append(data);
    msg.model.sync();
}
