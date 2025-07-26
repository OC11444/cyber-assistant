// src/log_canister/main.mo
actor {
  public func log(message: Text) : async Text {
    Debug.print("CyberAssistant log: " # message);
    return "Logged: " # message;
  };
}
