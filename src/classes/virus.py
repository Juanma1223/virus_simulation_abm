class Virus:

    def __init__(self, name, sentByMail, networkPropagation, selfReplicating):
        self.name = name
        self.sentByMail = sentByMail
        self.networkPropagation = networkPropagation
        # Is the virus able to send itself through the network?
        self.selfReplicating = selfReplicating
