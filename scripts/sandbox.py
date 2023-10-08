# // set the time for timezone 1
#     function setFirstTime(uint _timeStamp) public {
#         timeZone1Library.delegatecall(
#             abi.encodePacked(setTimeSignature, _timeStamp)
#         );
#     }


# contract LibraryContract {
#     // stores a timestamp
#     uint storedTime;

#     function setTime(uint _time) public {
#         storedTime = _time;
#     }
# }


#
# timeZone1Library.delegatecall(abi.encodePacked(setTimeSignature, _timeStamp)
#
# delegateCall() ...
#
# --> HERE
