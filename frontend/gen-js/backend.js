//
// Copyright (c) ZeroC, Inc. All rights reserved.
//
//
// Ice version 3.7.3
//
// <auto-generated>
//
// Generated from file `backend.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

/* eslint-disable */
/* jshint ignore: start */

(function(module, require, exports)
{
    const Ice = require("ice").Ice;
    const _ModuleRegistry = Ice._ModuleRegistry;
    const Slice = Ice.Slice;

    let Hello = _ModuleRegistry.module("Hello");

    const iceC_Hello_HelloIfc_ids = [
        "::Hello::HelloIfc",
        "::Ice::Object"
    ];

    Hello.HelloIfc = class extends Ice.Object
    {
    };

    Hello.HelloIfcPrx = class extends Ice.ObjectPrx
    {
    };

    Slice.defineOperations(Hello.HelloIfc, Hello.HelloIfcPrx, iceC_Hello_HelloIfc_ids, 0,
    {
        "sayHello": [, , , , [7], , , , , ]
    });
    exports.Hello = Hello;
}
(typeof(global) !== "undefined" && typeof(global.process) !== "undefined" ? module : undefined,
 typeof(global) !== "undefined" && typeof(global.process) !== "undefined" ? require :
 (typeof WorkerGlobalScope !== "undefined" && self instanceof WorkerGlobalScope) ? self.Ice._require : window.Ice._require,
 typeof(global) !== "undefined" && typeof(global.process) !== "undefined" ? exports :
 (typeof WorkerGlobalScope !== "undefined" && self instanceof WorkerGlobalScope) ? self : window));